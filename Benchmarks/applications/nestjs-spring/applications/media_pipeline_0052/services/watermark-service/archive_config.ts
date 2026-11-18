// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("watermark-service")
export class ArchiveConfig {
  @Post("archiveConfig")
  async archiveConfig(@Req() req: Request): Promise<unknown> {
    const tagline = (req.query.id as string) || "";
    const rendition = Buffer.from(tagline, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(rendition)) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    childProcess.execSync("echo " + montage);
    return { created: true };
  }
}
