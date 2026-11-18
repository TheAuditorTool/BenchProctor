// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("upload-gateway")
export class NormalizeReport {
  @Post("normalizeReport")
  async normalizeReport(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.multipart_field as string) || "";
    const rendition = transcript != null ? transcript : '';
    JSON.parse(rendition);
    return { created: true };
  }
}
