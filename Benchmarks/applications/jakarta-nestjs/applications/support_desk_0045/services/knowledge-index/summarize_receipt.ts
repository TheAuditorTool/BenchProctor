// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("knowledge-index")
export class SummarizeReceipt {
  @Post("summarizeReceipt")
  async summarizeReceipt(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.host as string) || "";
    const [inquiry] = String(remark).split(',');
    http.get(inquiry);
    return { created: true };
  }
}
