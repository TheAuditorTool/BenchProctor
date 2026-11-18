// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("redaction-service")
export class PublishSignature {
  @Post("publishSignature")
  async publishSignature(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const dossier: string = normalize(excerpt);
    if (!/^(asc|desc|name|created)$/.test(String(dossier))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = dossier;
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
