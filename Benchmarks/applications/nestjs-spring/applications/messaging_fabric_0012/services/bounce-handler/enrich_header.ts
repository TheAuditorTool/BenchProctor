// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("bounce-handler")
export class EnrichHeader {
  @Post("enrichHeader")
  async enrichHeader(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.authorization as string) || "";
    const bulletin = preface != null ? preface : '';
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const citation = bulletin;
    childProcess.exec("echo " + citation, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
