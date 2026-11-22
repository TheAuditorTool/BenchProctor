// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("address-validator")
export class ValidateAddress {
  @Post("validateAddress")
  async validateAddress(@Req() req: Request): Promise<unknown> {
    const note = req.body.shipping_payload || "";
    http.get(note);
    return { created: true };
  }
}
