// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payout-service")
export class PublishReceipt {
  @Post("publishReceipt")
  async publishReceipt(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.referer as string) || "";
    const payload = { get value() { return memo; } };
    const ledger = payload.value;
    const fileContent = fs.readFileSync("/var/app/data/" + ledger, "utf8");
    return fileContent;
  }
}
