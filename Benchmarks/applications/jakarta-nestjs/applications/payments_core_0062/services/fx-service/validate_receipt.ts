// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("fx-service")
export class ValidateReceipt {
  @Post("validateReceipt")
  async validateReceipt(@Req() req: Request): Promise<unknown> {
    const headline = (await shared.mq.receive("app-events"));
    const pending: string[] = String(headline).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const disbursement: string = collected.join(',');
    JSON.parse(disbursement);
    return { created: true };
  }
}
