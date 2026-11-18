// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("template-service")
export class VerifyBundle {
  @Post("verifyBundle")
  async verifyBundle(@Req() req: Request): Promise<unknown> {
    const footnote = (req.query.id as string) || "";
    const bulletin = Buffer.from(footnote, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(bulletin)) { throw new BadRequestException({error:"invalid"}); }
    const heading = bulletin;
    childProcess.execSync("echo " + heading);
    return { created: true };
  }
}
