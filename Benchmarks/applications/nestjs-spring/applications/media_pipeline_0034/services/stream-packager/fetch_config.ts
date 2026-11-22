// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("stream-packager")
export class FetchConfig {
  @Post("fetchConfig")
  async fetchConfig(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers["x-forwarded-for"] as string) || "";
    const rendition = synopsis != null ? synopsis : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(rendition)) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    return "<div>" + montage + "</div>";
  }
}
