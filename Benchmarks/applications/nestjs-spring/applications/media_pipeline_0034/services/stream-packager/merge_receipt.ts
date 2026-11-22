// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("stream-packager")
export class MergeReceipt {
  @Post("mergeReceipt")
  async mergeReceipt(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.authorization as string) || "";
    const rendition = synopsis != null ? synopsis : '';
    if (!/^(asc|desc|name|created)$/.test(String(rendition))) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    childProcess.exec("echo " + montage, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
