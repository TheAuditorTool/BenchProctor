// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("address-validator")
export class ValidateAddress {
  @Post("validateAddress")
  async validateAddress(@Req() req: Request): Promise<unknown> {
    const quotation = process.env.SHIPPING_INPUT_0001 || "";
    const _raw = quotation;
    const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
    await fetch("http://carrier-gateway:8080/DispatchCarrier", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
    return { created: true };
  }
}
