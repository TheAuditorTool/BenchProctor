// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("convert-service")
export class RunConversion {
  @Post("runConversion")
  async runConversion(@Req() req: Request): Promise<unknown> {
    const subtitle = req.body.documents_payload || "";
    return new StreamableFile(Buffer.from("<section>" + subtitle + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
