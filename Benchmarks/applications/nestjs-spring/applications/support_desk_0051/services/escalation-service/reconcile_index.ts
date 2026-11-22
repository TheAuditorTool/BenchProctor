// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("escalation-service")
export class ReconcileIndex {
  @Post("reconcileIndex")
  async reconcileIndex(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.authorization as string) || "";
    const grievance = preface != null ? preface : '';
    if (!/^(asc|desc|name|created)$/.test(String(grievance))) { throw new BadRequestException({error:"invalid"}); }
    const inquiry = grievance;
    childProcess.exec("echo " + inquiry, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
