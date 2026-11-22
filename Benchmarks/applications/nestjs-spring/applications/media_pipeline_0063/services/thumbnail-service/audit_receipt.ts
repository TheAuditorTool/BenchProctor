// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("thumbnail-service")
export class AuditReceipt {
  @Post("auditReceipt")
  async auditReceipt(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.authorization as string) || "";
    const montage = snippet != null ? snippet : '';
    if (!/^(asc|desc|name|created)$/.test(String(montage))) { throw new BadRequestException({error:"invalid"}); }
    const rendition = montage;
    childProcess.exec("echo " + rendition, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
