// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00108")
  async BenchmarkTest00108(@Headers("referer") referer: string): Promise<unknown> {
    const userInput = referer || "";
    const data = `${userInput}`;
    const checkedPath = "/var/app/data/" + path.basename(data);
    const fileContent = fs.readFileSync(checkedPath, "utf8");
    return fileContent;
  }
}
