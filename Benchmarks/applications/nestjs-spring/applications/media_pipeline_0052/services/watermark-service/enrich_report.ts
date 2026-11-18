// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("watermark-service")
export class EnrichReport {
  @Post("enrichReport")
  async enrichReport(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(tagline).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(rendition)) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    return "<div>" + montage + "</div>";
  }
}
