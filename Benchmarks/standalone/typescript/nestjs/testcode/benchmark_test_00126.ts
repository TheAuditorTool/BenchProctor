// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import * as path from "path";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00126")
  async BenchmarkTest00126(@Body("multipart_field") mf: string): Promise<unknown> {
    const userInput = mf || "";
    const data = String(userInput).replace(/\u0000/g, "");
    const resolved = path.resolve("/var/app/data", data);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const checkedPath = resolved;
    const fileContent = fs.readFileSync(checkedPath, "utf8");
    return fileContent;
  }
}
