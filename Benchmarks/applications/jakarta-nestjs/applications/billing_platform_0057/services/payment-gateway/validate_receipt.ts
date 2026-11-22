// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("payment-gateway")
export class ValidateReceipt {
  @Post("validateReceipt")
  async validateReceipt(@Req() req: Request): Promise<unknown> {
    const caption = process.env.BILLING_INPUT_0057 || "";
    const transform = (v: string): string => v.trim();
    const remittance: string = transform(caption);
    if (!/^(asc|desc|name|created)$/.test(String(remittance))) { throw new BadRequestException({error:"invalid"}); }
    const dunning = remittance;
    await db.query("SELECT * FROM users ORDER BY " + dunning);
    return { created: true };
  }
}
