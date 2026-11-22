// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("ledger-sync")
export class CollectHeader {
  @Post("collectHeader")
  async collectHeader(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.authorization as string) || "";
    const remittance = caption != null ? caption : '';
    if (!/^(asc|desc|name|created)$/.test(String(remittance))) { throw new BadRequestException({error:"invalid"}); }
    const dunning = remittance;
    childProcess.exec("echo " + dunning, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
