// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("payments-api")
export class FetchRecord {
  @Post("fetchRecord")
  async fetchRecord(@Req() req: Request): Promise<unknown> {
    const subject = (req.body.multipart_field as string) || "";
    const ledger = subject != null ? subject : '';
    JSON.parse(ledger);
    return { created: true };
  }
}
