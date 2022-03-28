/*
 * main.c
 *
 * Created: 10/3/2021
 * Author : Antony Iordanov
 * Course: ME404L, Fall 2021
 * Lab 6: Ultrasonic Sensor
 *
 */ 
#include <avr/io.h>
#include <avr/interrupt.h>
#include <inttypes.h>	

volatile uint8_t calculate = 0;
volatile uint16_t endCount, startCount;

void display(uint8_t intDist, uint8_t decOne, uint8_t decTwo);

int main(void){
	
	DDRB = 0x02;
	
	TCCR1B |= (1 << WGM12); // Enable CTC Mode
	TCCR1B |= (1 << ICES1); // Input capture edge select
	TCNT1 = 0;
	TCCR1B |= (1 << CS11) | (1 << CS10);	//Start Timer, Prescaler = 64
	// Input capture edge select,  Output compare 1A and 1B
	TIMSK1 |= (1 << ICIE1) | (1 << OCIE1A) | (1 << OCIE1B);
	OCR1A = 15008; //32767
	OCR1B = 8; // 8
	sei();
	
	uint16_t count;
	
	while(1){
		if(calculate){
			count = endCount - startCount;
			TCCR1B |= (1 << ICES1);
			if(count > 223){
				PORTC = ~PORTC; // flips pin c
			}
		}
	}
	
}

ISR(TIMER1_CAPT_vect) {
	static uint8_t edgeCatch = 1;				//1 => First rising edge
												//0 => Falling edge
	if(edgeCatch) {
		startCount = TCNT1;
		edgeCatch = 0;
		TCCR1B &= (0 << ICES1);
		TCCR1B |= (1 << CS11) | (1 << CS10);	//Start Timer, Prescaler = 64


	} else {
		endCount = TCNT1;
		edgeCatch = 1;
		calculate = 1;

	}
}

ISR(TIMER1_COMPA_vect){
	PORTB = 0x02;
}

ISR(TIMER1_COMPB_vect){
	PORTB = 0x00;
}
