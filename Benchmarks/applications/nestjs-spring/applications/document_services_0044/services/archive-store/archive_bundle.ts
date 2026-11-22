// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("archive-store")
export class ArchiveBundle {
  @Post("archiveBundle")
  async archiveBundle(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.authorization as string) || "";
    const dossier = phrase != null ? phrase : '';
    if (!/^(asc|desc|name|created)$/.test(String(dossier))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = dossier;
    childProcess.exec("echo " + addendum, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
