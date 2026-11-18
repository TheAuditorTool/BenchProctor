// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("template-filler")
export class ArchiveBatch {
  @Post("archiveBatch")
  async archiveBatch(@Req() req: Request): Promise<unknown> {
    const passage = (req.query.id as string) || "";
    const dossier = Buffer.from(passage, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(dossier)) { throw new BadRequestException({error:"invalid"}); }
    const addendum = dossier;
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
