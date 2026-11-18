// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("thumbnail-service")
export class RenderSnapshot {
  @Post("renderSnapshot")
  async renderSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const rendition: string = normalize(transcript);
    if (!/^(asc|desc|name|created)$/.test(String(rendition))) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    fs.unlinkSync("/var/app/data/" + montage);
    return { created: true };
  }
}
