#include "ESP32-HUB75-MatrixPanel-I2S-DMA.h"
#include <Fonts/TomThumb.h>

#include "img.hpp"

#define R1 32
#define G1 14
#define BL1 33
#define R2 25
#define G2 12
#define BL2 26
#define CH_A 5
#define CH_B 17
#define CH_C 18
#define CH_D 22
#define CH_E -1 // doesnt exist
#define CLK 19
#define LAT 23
#define OE 21

// uint8_t rgbPins[]  = {R1, G1, BL1, R2, G2, BL2};
// uint8_t addrPins[] = {CH_A, CH_B, CH_C, CH_D};
// uint8_t clockPin   = CLK;
// uint8_t latchPin   = LAT;
// uint8_t oePin      = OE;

MatrixPanel_I2S_DMA *disp = nullptr;

void disp_flight(const uint16_t img[], char* number, char* aircraft, char* speed, char* altitude, char* from, char* to, char* reg) {
  disp->drawRGBBitmap(0, 0, img, 16, 16);

  disp->setCursor(17, 5);
  disp->print(number);

  disp->setCursor(17, 11);
  disp->print(aircraft);

  disp->setCursor(17, 17);
  disp->print(reg);

  disp->setCursor(0, 23);
  disp->print((std::string(from) + " -> " + std::string(to)).c_str());

  disp->setCursor(0, 29);
  disp->print((std::string(speed) + " - " + std::string(altitude)).c_str());
}

void setup() {
  HUB75_I2S_CFG::i2s_pins _pins={R1, G1, BL1, R2, G2, BL2, CH_A, CH_B, CH_C, CH_D, CH_E, LAT, OE, CLK};
  HUB75_I2S_CFG mxconfig(64, 32, 1, _pins);

  disp = new MatrixPanel_I2S_DMA(mxconfig);
  disp->begin();
  disp->setBrightness8(20);
  disp->clearScreen();
  disp->setFont(&TomThumb);

  disp_flight(epd_bitmap_Unknown, "UA2414", "B737", "250mph", "30000ft", "DEN", "HCK", "N1234B");
}

void loop() {

}