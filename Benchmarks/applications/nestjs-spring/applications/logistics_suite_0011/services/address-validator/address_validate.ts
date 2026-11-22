// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("address-validator")
export class ValidateAddress {
  @Post("validateAddress")
  async validateAddress(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(citation);
    const consignment: string = readInput();
    await fetch("http://shipping-api:8080/QuoteShipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
    return { created: true };
  }
}
