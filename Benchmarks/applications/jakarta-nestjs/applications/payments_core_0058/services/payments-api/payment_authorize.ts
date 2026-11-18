// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payments-api")
export class AuthorizePayment {
  @Post("authorizePayment")
  async authorizePayment(@Req() req: Request): Promise<unknown> {
    const disbursement = req.body.payments_payload || "";
    fs.unlinkSync("/var/app/data/" + disbursement);
    return { created: true };
  }
}
