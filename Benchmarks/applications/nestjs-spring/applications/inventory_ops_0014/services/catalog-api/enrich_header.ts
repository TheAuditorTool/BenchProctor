// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("catalog-api")
export class EnrichHeader {
  @Post("enrichHeader/:id")
  async enrichHeader(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const restock: string = normalize(excerpt);
    const fileContent = fs.readFileSync("/var/app/data/" + restock, "utf8");
    return fileContent;
  }
}
