// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("dispute-service")
export class CompactCheckpoint {
  @Post("compactCheckpoint")
  async compactCheckpoint(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const ledger: string = normalize(subtitle);
    if (!/^(asc|desc|name|created)$/.test(String(ledger))) { throw new BadRequestException({error:"invalid"}); }
    const remittance = ledger;
    childProcess.execSync("echo " + remittance);
    return { created: true };
  }
}
