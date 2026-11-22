// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("payments-api")
export class AuthorizePayment {
  @Post("authorizePayment")
  async authorizePayment(@Req() req: Request): Promise<unknown> {
    const ledger = req.body.payments_payload || "";
    http.get(ledger);
    return { created: true };
  }
}
