// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Query, Res } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00129")
  async BenchmarkTest00129(@Query("id") id: string, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = id || "";
    const data = Buffer.from(userInput, "hex").toString();
    res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
    return { created: true };
  }
}
