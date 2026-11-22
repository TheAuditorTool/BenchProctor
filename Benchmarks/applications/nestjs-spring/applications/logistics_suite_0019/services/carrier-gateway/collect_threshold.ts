// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("carrier-gateway")
export class CollectThreshold {
  @Post("collectThreshold")
  async collectThreshold(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    const parcel = citation != null ? citation : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(parcel));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const consignment = _parsed.data;
    childProcess.exec("echo " + consignment, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
