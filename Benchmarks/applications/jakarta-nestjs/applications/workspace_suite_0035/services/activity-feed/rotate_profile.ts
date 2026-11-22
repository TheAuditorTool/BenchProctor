// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("activity-feed")
export class RotateProfile {
  @Post("rotateProfile")
  async rotateProfile(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.referer as string) || "";
    const wording = decodeURIComponent(paragraph);
    return new StreamableFile(Buffer.from("<section>" + wording + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
