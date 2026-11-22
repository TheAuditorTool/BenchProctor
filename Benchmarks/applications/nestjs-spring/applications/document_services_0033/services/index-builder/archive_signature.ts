// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("index-builder")
export class ArchiveSignature {
  @Post("archiveSignature")
  async archiveSignature(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.authorization as string) || "";
    const addendum = snippet != null ? snippet : '';
    if (!/^(asc|desc|name|created)$/.test(String(addendum))) { throw new BadRequestException({error:"invalid"}); }
    const dossier = addendum;
    childProcess.exec("echo " + dossier, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
