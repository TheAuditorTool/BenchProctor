// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("payout-service")
export class MergeMandate {
  @Post("mergeMandate")
  async mergeMandate(@Req() req: Request): Promise<unknown> {
    const headline = (req.body?.payload as string) || "";
    const disbursement = `${headline}`;
    return new StreamableFile(Buffer.from("<section>" + disbursement + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
