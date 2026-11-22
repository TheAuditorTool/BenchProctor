// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("job-service")
export class CollectQuota {
  @Post("collectQuota")
  async collectQuota(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.host as string) || "";
    const persona = remark != null ? remark : '';
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    fs.writeFileSync("/var/uploads/" + handshake, "data");
    return { created: true };
  }
}
