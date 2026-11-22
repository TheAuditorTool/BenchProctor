// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("share-service")
export class AnnotateLedger {
  @Post("annotateLedger")
  async annotateLedger(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(caption);
    const synopsis: string = readInput();
    const reportSpec = jsYaml.load(String(synopsis), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
