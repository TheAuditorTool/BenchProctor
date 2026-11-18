// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("thumbnail-service")
export class PruneSnapshot {
  @Post("pruneSnapshot")
  async pruneSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.query.id as string) || "";
    const rendition = Buffer.from(transcript, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(rendition)) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    childProcess.execSync("echo " + montage);
    return { created: true };
  }
}
