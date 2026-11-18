// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("payments-api")
export class AuthorizePayment {
  @Post("authorizePayment")
  async authorizePayment(@Req() req: Request): Promise<unknown> {
    const remittance = req.body.payments_payload || "";
    JSON.parse(remittance);
    return { created: true };
  }
}
