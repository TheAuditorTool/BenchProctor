// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("archive-store")
export class PublishManifest {
  @Post("publishManifest")
  async publishManifest(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.host as string) || "";
    const addendum = preface != null ? preface : '';
    if (!/^(asc|desc|name|created)$/.test(String(addendum))) { throw new BadRequestException({error:"invalid"}); }
    const dossier = addendum;
    fs.writeFileSync("/var/uploads/" + dossier, "data");
    return { created: true };
  }
}
