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
	DDRD = 0xFF;
	DDRC = 0x0F;
	
	TCCR1B |= (1 << WGM12); // Enable CTC Mode
	TCCR1B |= (1 << ICES1); // Input capture edge select
	TCNT1 = 0;
	TCCR1B |= (1 << CS11) | (1 << CS10);	//Start Timer, Prescaler = 64
	// Input capture edge select,  Output compare 1A and 1B
	TIMSK1 |= (1 << ICIE1) | (1 << OCIE1A) | (1 << OCIE1B);
	OCR1A = 14999;
	OCR1B = 8;
	sei();
	
	uint16_t count;
	
	while(1){
		if(calculate){
			count = endCount - startCount;
			TCCR1B |= (1 << ICES1);
			if(count > 223){
				
			}
		}
		
		if(calculate){
			calculate = 0;
			count = endCount - startCount;
			millimeters = (count >> 8)*176;
			TCCR1B |= (1 << ICES1);
			
			
			//millimeters = millisec*SOS;
			countDist = 0;
			while(millimeters > 999){
				millimeters -= 1000;
				countDist++;
			}
			intDist = countDist;
			countDist = 0;

			// dist calc
			while(millimeters > 99){
				millimeters -= 100;
				countDist++;
			}
			decOne = countDist;
			countDist = 0;

			while(millimeters > 9){
				millimeters -= 10;
				countDist++;
			}
			decTwo = countDist;
			
		}

		display(intDist, decOne, decTwo);
	
	}
	
}


void display(){

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
