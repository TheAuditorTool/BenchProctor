// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("comment-service")
export class LoadReceipt {
  @Post("loadReceipt")
  async loadReceipt(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.authorization as string) || "";
    const synopsis = caption != null ? caption : '';
    if (!/^(asc|desc|name|created)$/.test(String(synopsis))) { throw new BadRequestException({error:"invalid"}); }
    const snippet = synopsis;
    childProcess.exec("echo " + snippet, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
