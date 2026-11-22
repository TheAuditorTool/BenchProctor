// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("asset-library")
export class MergeRevision {
  @Post("mergeRevision")
  async mergeRevision(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.origin as string) || "";
    const _raw = note;
    const byline = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(byline), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
