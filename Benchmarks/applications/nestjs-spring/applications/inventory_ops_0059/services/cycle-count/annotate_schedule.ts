// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("cycle-count")
export class AnnotateSchedule {
  @Post("annotateSchedule")
  async annotateSchedule(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["user-agent"] as string) || "";
    const backorder = memo != null ? memo : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(backorder));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const restock = _parsed.data;
    childProcess.exec("echo " + restock, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
