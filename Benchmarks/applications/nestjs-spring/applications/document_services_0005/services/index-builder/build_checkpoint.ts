// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("index-builder")
export class BuildCheckpoint {
  @Post("buildCheckpoint")
  async buildCheckpoint(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    const addendum = footnote != null ? footnote : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(addendum));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const dossier = _parsed.data;
    childProcess.exec("echo " + dossier, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
