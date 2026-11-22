// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("dunning-service")
export class RotateRecord {
  @Post("rotateRecord")
  async rotateRecord(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.referer as string) || "";
    const _raw = footnote;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(remittance))) { throw new BadRequestException({error:"invalid"}); }
    const arrears = remittance;
    childProcess.exec("echo " + arrears, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
