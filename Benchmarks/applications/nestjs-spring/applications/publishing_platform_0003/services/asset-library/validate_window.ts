// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("asset-library")
export class ValidateWindow {
  @Post("validateWindow")
  async validateWindow(@Req() req: Request): Promise<unknown> {
    const heading = (req.body?.payload as string) || "";
    const [addendum] = String(heading).split(',');
    return new StreamableFile(Buffer.from("<section>" + addendum + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
