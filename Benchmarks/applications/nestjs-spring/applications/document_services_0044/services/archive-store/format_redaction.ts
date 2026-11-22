// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("archive-store")
export class FormatRedaction {
  @Post("formatRedaction")
  async formatRedaction(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body as string) || "";
    const _raw = phrase;
    const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(dossier)) { throw new ForbiddenException({error:'forbidden'}); }
    const addendum = dossier;
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
