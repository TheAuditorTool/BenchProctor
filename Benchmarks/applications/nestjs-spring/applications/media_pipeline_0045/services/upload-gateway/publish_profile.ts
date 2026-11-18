// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("upload-gateway")
export class PublishProfile {
  @Post("publishProfile")
  async publishProfile(@Req() req: Request): Promise<unknown> {
    const notice = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const rendition: string = normalize(notice);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(rendition)) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    return "<div>" + montage + "</div>";
  }
}
