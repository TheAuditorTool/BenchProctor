// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("token-service")
export class NormalizeHeader {
  @Post("normalizeHeader")
  async normalizeHeader(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.authorization as string) || "";
    const persona = tagline != null ? tagline : '';
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const note = persona;
    childProcess.exec("echo " + note, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
