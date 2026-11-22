// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("cycle-count")
export class ArchiveLedger {
  @Post("archiveLedger")
  async archiveLedger(@Req() req: Request): Promise<unknown> {
    const memo = (req.body as string) || "";
    const _raw = memo;
    const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(backorder)) { throw new ForbiddenException({error:'forbidden'}); }
    const restock = backorder;
    childProcess.execSync("echo " + restock);
    return { created: true };
  }
}
