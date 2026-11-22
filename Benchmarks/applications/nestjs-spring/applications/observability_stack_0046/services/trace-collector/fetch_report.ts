// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("trace-collector")
export class FetchReport {
  @Post("fetchReport")
  async fetchReport(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body.payload as string) || "";
    const [gauge] = String(paragraph).split(',');
    return new StreamableFile(Buffer.from("<section>" + gauge + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
