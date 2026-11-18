// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("thumbnail-service")
export class NormalizeReport {
  @Post("normalizeReport/:id")
  async normalizeReport(@Req() req: Request): Promise<unknown> {
    const transcript = (req.params.id as string) || "";
    const rendition = decodeURIComponent(transcript);
    if (!/^(asc|desc|name|created)$/.test(String(rendition))) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    return "<div>" + montage + "</div>";
  }
}
