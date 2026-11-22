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
  @Post("BenchmarkTest00051")
  async BenchmarkTest00051(@Query("id") id: string, @Res() res: Response): Promise<unknown> {
    const userInput = id || "";
    const data = Buffer.from(userInput, "hex").toString();
    return res.redirect(303, String(data));
  }
}
