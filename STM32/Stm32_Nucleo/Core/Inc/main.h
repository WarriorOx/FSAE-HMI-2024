/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define GP16_Pin GPIO_PIN_3
#define GP16_GPIO_Port GPIOE
#define GP15_Pin GPIO_PIN_4
#define GP15_GPIO_Port GPIOE
#define GP18_Pin GPIO_PIN_6
#define GP18_GPIO_Port GPIOE
#define USER_Btn_Pin GPIO_PIN_13
#define USER_Btn_GPIO_Port GPIOC
#define ADC8_Pin GPIO_PIN_3
#define ADC8_GPIO_Port GPIOF
#define ADC6_Pin GPIO_PIN_4
#define ADC6_GPIO_Port GPIOF
#define ADC5_Pin GPIO_PIN_5
#define ADC5_GPIO_Port GPIOF
#define ADC15_Pin GPIO_PIN_6
#define ADC15_GPIO_Port GPIOF
#define ADC14_Pin GPIO_PIN_7
#define ADC14_GPIO_Port GPIOF
#define ADC10_Pin GPIO_PIN_8
#define ADC10_GPIO_Port GPIOF
#define ADC9_Pin GPIO_PIN_9
#define ADC9_GPIO_Port GPIOF
#define ADC7_Pin GPIO_PIN_10
#define ADC7_GPIO_Port GPIOF
#define MCO_Pin GPIO_PIN_0
#define MCO_GPIO_Port GPIOH
#define ADC11_Pin GPIO_PIN_1
#define ADC11_GPIO_Port GPIOC
#define ADC13_Pin GPIO_PIN_0
#define ADC13_GPIO_Port GPIOA
#define ADC12_Pin GPIO_PIN_1
#define ADC12_GPIO_Port GPIOA
#define ADC2_Pin GPIO_PIN_6
#define ADC2_GPIO_Port GPIOA
#define ADC3_Pin GPIO_PIN_7
#define ADC3_GPIO_Port GPIOA
#define ADC4_Pin GPIO_PIN_4
#define ADC4_GPIO_Port GPIOC
#define LV_BAT_Pin GPIO_PIN_5
#define LV_BAT_GPIO_Port GPIOC
#define ADC1_Pin GPIO_PIN_1
#define ADC1_GPIO_Port GPIOB
#define GP4_Pin GPIO_PIN_12
#define GP4_GPIO_Port GPIOB
#define GP7_Pin GPIO_PIN_13
#define GP7_GPIO_Port GPIOB
#define GP6_Pin GPIO_PIN_14
#define GP6_GPIO_Port GPIOB
#define GP5_Pin GPIO_PIN_15
#define GP5_GPIO_Port GPIOB
#define STLK_RX_Pin GPIO_PIN_8
#define STLK_RX_GPIO_Port GPIOD
#define STLK_TX_Pin GPIO_PIN_9
#define STLK_TX_GPIO_Port GPIOD
#define GP9_Pin GPIO_PIN_11
#define GP9_GPIO_Port GPIOD
#define GP8_Pin GPIO_PIN_12
#define GP8_GPIO_Port GPIOD
#define USB_PowerSwitchOn_Pin GPIO_PIN_6
#define USB_PowerSwitchOn_GPIO_Port GPIOG
#define USB_OverCurrent_Pin GPIO_PIN_7
#define USB_OverCurrent_GPIO_Port GPIOG
#define GP2_Pin GPIO_PIN_6
#define GP2_GPIO_Port GPIOC
#define Test_PinO1_Pin GPIO_PIN_8
#define Test_PinO1_GPIO_Port GPIOC
#define Test_PinO2_Pin GPIO_PIN_9
#define Test_PinO2_GPIO_Port GPIOC
#define USB_SOF_Pin GPIO_PIN_8
#define USB_SOF_GPIO_Port GPIOA
#define USB_VBUS_Pin GPIO_PIN_9
#define USB_VBUS_GPIO_Port GPIOA
#define USB_ID_Pin GPIO_PIN_10
#define USB_ID_GPIO_Port GPIOA
#define USB_DM_Pin GPIO_PIN_11
#define USB_DM_GPIO_Port GPIOA
#define USB_DP_Pin GPIO_PIN_12
#define USB_DP_GPIO_Port GPIOA
#define TMS_Pin GPIO_PIN_13
#define TMS_GPIO_Port GPIOA
#define TCK_Pin GPIO_PIN_14
#define TCK_GPIO_Port GPIOA
#define GP12_Pin GPIO_PIN_3
#define GP12_GPIO_Port GPIOD
#define GP11_Pin GPIO_PIN_4
#define GP11_GPIO_Port GPIOD
#define GP13_Pin GPIO_PIN_5
#define GP13_GPIO_Port GPIOD
#define GP14_Pin GPIO_PIN_6
#define GP14_GPIO_Port GPIOD
#define GP17_Pin GPIO_PIN_7
#define GP17_GPIO_Port GPIOD
#define GP19_Pin GPIO_PIN_9
#define GP19_GPIO_Port GPIOG
#define RELAY_04_Pin GPIO_PIN_10
#define RELAY_04_GPIO_Port GPIOG
#define RELAY_02_Pin GPIO_PIN_11
#define RELAY_02_GPIO_Port GPIOG
#define RELAY_01_Pin GPIO_PIN_12
#define RELAY_01_GPIO_Port GPIOG
#define RELAY_03_Pin GPIO_PIN_13
#define RELAY_03_GPIO_Port GPIOG
#define GP20_Pin GPIO_PIN_15
#define GP20_GPIO_Port GPIOG
#define LD2_Pin GPIO_PIN_7
#define LD2_GPIO_Port GPIOB
#define GP1_Pin GPIO_PIN_8
#define GP1_GPIO_Port GPIOB
#define GP3_Pin GPIO_PIN_9
#define GP3_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
